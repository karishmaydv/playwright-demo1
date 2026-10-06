import {test, expect} from '@playwright/test';
test('Test1', async ({page}) => {
    console.log('.. iam in Test1..');
  await page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login');
  await expect(page).toHaveTitle(/OrangeHRM/);
}
)
;
test('Test2', async ({page}) => {
    console.log('.. iam in Test2..');
    await page.goto('https://google.com');