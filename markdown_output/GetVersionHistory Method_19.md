Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVersionHistory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [BufferedRuleWithVersionHistory Class](topic6035.md) : GetVersionHistory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the version history for the rule. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Function GetVersionHistory() As [RuleVersionDetails()](topic5277.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [BufferedRuleWithVersionHistory](topic6035.md)
    Dim value() As [RuleVersionDetails](topic5277.md)
     
    value = instance.GetVersionHistory()  
  
C#|   
---|---  
      
    
    public virtual [RuleVersionDetails[]](topic5277.md) GetVersionHistory()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[BufferedRuleWithVersionHistory Class](topic6035.md)   
[BufferedRuleWithVersionHistory Members](topic6036.md)


