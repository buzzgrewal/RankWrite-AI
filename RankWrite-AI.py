import streamlit as st
from huggingface_hub import InferenceClient

def generate_blog_post(topic: str, api_key: str) -> str:
  

    client = InferenceClient(api_key=api_key)
    

    prompt = (
        f"You are an expert content writer. Write a detailed, SEO-optimized blog post about '{topic}'.\n"
        "The article should include:\n"
        "  - An attention-grabbing headline.\n"
        "  - A compelling introduction.\n"
        "  - Several well-structured subheadings.\n"
        "  - Engaging and informative content with proper keyword usage for SEO without compromising readability.\n"
        "  - A concise conclusion.\n"
        "The blog post should be ready to publish on platforms like WordPress or Medium."
    )
    

    messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]
    

    try:
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Qwen-32B", 
            messages=messages
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating blog post: {e}"

def main():
    st.title("RankWrite AI")
    st.markdown(
        """
        Generate a detailed, SEO-optimized blog with keyword post 
        on any topic you provide using DeepSeek R1 reasoning model.
        """
    )
    
  
    st.sidebar.header("Configuration")
    api_key = st.sidebar.text_input("Hugging Face API Key", type="password", help="Enter your Hugging Face API key")
    
 
    topic = st.text_input("Enter the blog topic:", "The Future of Artificial Intelligence in Healthcare")
    

    if st.button("Generate Blog Post"):
        if not api_key:
            st.error("Please enter your Hugging Face API key in the sidebar.")
        elif not topic:
            st.error("Please enter a topic for the blog post.")
        else:
            with st.spinner("Generating blog post..."):
                blog_post = generate_blog_post(topic, api_key)
            st.success("Blog post generated!")
            st.markdown("### Generated Blog Post")
            st.write(blog_post)

if __name__ == "__main__":
    main()
