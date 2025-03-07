Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetVersionHistory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Utility Namespace](topic13190.md) > [SearchItem Class](topic13270.md) : GetVersionHistory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected MustOverride Function GetVersionHistory() As [RuleVersionDetails()](topic5277.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SearchItem](topic13270.md)
    Dim value() As [RuleVersionDetails](topic5277.md)
     
    value = instance.GetVersionHistory()  
  
C#|   
---|---  
      
    
    protected abstract [RuleVersionDetails[]](topic5277.md) GetVersionHistory()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SearchItem Class](topic13270.md)   
[SearchItem Members](topic13271.md)


