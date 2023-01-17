import os

import os

def convert_to_html(question_list):
    html = '<form id="quiz-form">\n'
    for i, question in enumerate(question_list):
        html += '    <div id="question{}" class="question">\n'.format(i+1)
        html += '      <p>Question {}</p>\n'.format(i+1)
        html += '      <p>' + question.split("\n")[0] + '</p>\n'
        for j, option in enumerate(question.split("\n")[1:]):
            html += '      <label>\n'
            html += '        <input type="radio" name="question{}" value="{}">\n'.format(i+1, chr(ord('A') + j))
            html += '        ' + option + '\n'
            html += '      </label>\n'
            html += '      <br>\n'
        html += '      <button type="button" class="next-btn">Next</button>\n'
        html += '    </div>\n'
    html += '</form>'
    return html

def main():
    #input file name
    input_file_name = input("Enter the name of the file containing the questions: ")
    #read the input file
    with open(input_file_name, 'r') as input_file:
        questions = input_file.read().split("\n\n")
    #output file name
    output_file_name = input("Enter the name of the file to save the HTML: ")
    #write the HTML to the output file
    with open(output_file_name, 'w') as output_file:
        output_file.write(convert_to_html(questions))
    #Ask if there are more questions
    while input("Are there more questions to process? (y/n): ") == 'y':
        input_file_name = input("Enter the name of the file containing the questions: ")
        with open(input_file_name, 'r') as input_file:
            questions = input_file.read().split("\n\n")
        output_file_name = input("Enter the name of the file to save the HTML: ")
        with open(output_file_name, 'w') as output_file:
            output_file.write(convert_to_html(questions))
    print("Processing completed.")

if __name__ == '__main__':
    main()
