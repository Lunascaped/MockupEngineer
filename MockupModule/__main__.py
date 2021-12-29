import os

from MockupModule import MockupEngineer


def main():
    mockup = MockupEngineer()
    i = 0
    for template in mockup.templates:
        print('[{}] {} {} ({})'.format(i, template.manufacturer, template.name, template.year))
        i += 1
    template = mockup.templates[int(input('Choose device: '))]
    print('- - - - - - - - - -')
    i = 0
    for color in template.colors:
        print('[{}] {}'.format(i, color.color))
        i += 1
    color = template.colors[int(input('Choose color: '))].color
    print('- - - - - - - - - -')
    screenshot = input('Enter path to screenshot: ')
    print('- - - - - - - - - -\nWorking...')
    mockup = mockup.generate(template, screenshot, color)
    print('- - - - - - - - - -\nSuccess: {}'.format(mockup))
    os.system('open {}'.format(mockup))


if __name__ == '__main__':
    main()
