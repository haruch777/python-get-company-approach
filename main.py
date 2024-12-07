import os
from modules.web_search import search_company_website
from modules.web_scraper import scrape_company_info
from modules.ai_analyzer import analyze_company_data
from modules.config import load_config

def main():
    # Load configuration
    config = load_config()
    
    # Get company name from user
    company_name = input("企業名を入力してください: ")
    
    try:
        # Search for company website
        print(f"{company_name}の情報を検索中...")
        website_url = search_company_website(company_name)
        
        if not website_url:
            print("企業のウェブサイトが見つかりませんでした。")
            return
            
        # Scrape company information
        print("企業情報を収集中...")
        company_info = scrape_company_info(website_url)
        
        # Analyze data and generate approach suggestions
        print("営業アプローチを生成中...")
        approach_suggestions = analyze_company_data(company_info)
        
        # Display results
        print("\n=== 営業アプローチ提案 ===")
        print(approach_suggestions)
        
    except Exception as e:
        print(f"エラーが発生しました: {str(e)}")

if __name__ == "__main__":
    main()