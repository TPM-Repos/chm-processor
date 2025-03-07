Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
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

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTokens( _
       ByVal _ruleText_ As String _
    ) As IEnumerable(Of RuleToken)  
  
Visual Basic (Usage)| Copy Code  
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

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


