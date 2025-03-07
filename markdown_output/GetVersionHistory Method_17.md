Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVersionHistory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Abstractions Namespace](topic5939.md) > [IHasRuleVersionHistory Interface](topic5975.md) : GetVersionHistory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the version history for the item. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetVersionHistory() As [RuleVersionDetails()](topic5277.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IHasRuleVersionHistory](topic5975.md)
    Dim value() As [RuleVersionDetails](topic5277.md)
     
    value = instance.GetVersionHistory()  
  
C#|   
---|---  
      
    
    [RuleVersionDetails[]](topic5277.md) GetVersionHistory()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IHasRuleVersionHistory Interface](topic5975.md)   
[IHasRuleVersionHistory Members](topic5976.md)


