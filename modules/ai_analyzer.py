import os
import openai
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

def analyze_company_data(company_info):
    """
    Analyze company information using Azure OpenAI and generate approach suggestions
    """
    try:
        openai.api_type = "azure"
        openai.api_base = os.getenv('AZURE_OPENAI_ENDPOINT')
        openai.api_key = os.getenv('AZURE_OPENAI_KEY')
        openai.api_version = "2023-05-15"
        
        # Prepare prompt for Azure OpenAI
        prompt = f"""
        以下の企業情報に基づいて、効果的な営業アプローチを提案してください：
        
        企業URL: {company_info['url']}
        中期経営計画: {company_info['medium_term_plan']}
        事業戦略: {company_info['business_strategy']}
        企業ビジョン: {company_info['company_vision']}
        最近のニュース: {company_info['recent_news']}
        
        以下の点を考慮して提案を作成してください：
        1. 企業の現在の課題と目標
        2. 業界トレンドとの関連性
        3. 具体的なアプローチ方法
        4. 提案する製品・サービスの価値提案
        5. タイミングと優先順位
        """
        
        # Generate suggestions using Azure OpenAI
        response = openai.Completion.create(
            engine=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),
            prompt=prompt,
            max_tokens=1000,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None
        )
        
        return response.choices[0].text.strip()
        
    except Exception as e:
        print(f"AI分析中にエラーが発生しました: {str(e)}")
        return None