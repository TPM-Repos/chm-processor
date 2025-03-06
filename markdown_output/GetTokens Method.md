![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTokens Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : GetTokens Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_ruleText_
    The formula to retrieve the tokens from.

Glossary Item Box

Gets all tokens in the given formula. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTokens( _
       ByVal _ruleText_ As String _
    ) As IEnumerable(Of RuleToken)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim ruleText As String
    Dim value As IEnumerable(Of RuleToken)
     
    value = instance.GetTokens(ruleText)  
  
C#|   
---|---  
      
    
    public IEnumerable<RuleToken> GetTokens( 
       string _ruleText_
    )  
  
#### Parameters

 _ruleText_
    The formula to retrieve the tokens from.

#### Return Value

A list of the tokens that make up the given formula.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


