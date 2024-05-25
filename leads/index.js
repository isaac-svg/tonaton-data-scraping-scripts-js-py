import puppeteer from 'puppeteer';
import fs from 'fs/promises';
/**
 * @function scrape scrapes tonaton.com for leads
 */
async function scrape() {
  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto('http://mirror-h.org/archive/page/2');
    const content = await page.content();
    await fs.writeFile('./data.html', content);
    console.log(content);
  } catch (error) {
    console.log(error);
  }
}
// ?subject=Toyota Rav 4 2019/20 Assembled Brand New Bumper&body=https://jiji.com.gh/accra-metropolitan/car-parts-and-accessories/toyota-rav-4-2019-20-assembled-brand-new-bumper-acFxeHEPSwlN9MPg4OWyb6xn.html?utm_source=mail&utm_medium=site-share-button&utm_campaign=mailButton
// ?subject=2bdrm Apartment in East Legon for rent&body=https://jiji.com.gh/east-legon/houses-apartments-for-rent/2bdrm-apartment-in-east-legon-for-rent-yMjQqmMJfz2QVojYj6tvn2Do.html?utm_source=mail&utm_medium=site-share-button&utm_campaign=mailButton
//
// z-0lib
// @hTmCh8Ei]x~*@R
// vBU-E6kS:+6?4_h
scrape();
