       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Uses Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [SearchFinishedEventArgs Class](topic10317.md) : Uses Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets all uses in rules of the name we searched for. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Uses As [RuleSearchResult()](topic13227.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SearchFinishedEventArgs](topic10317.md)
    Dim value() As [RuleSearchResult](topic13227.md)
     
    value = instance.Uses  
  
C#|   
---|---  
      
    
    public [RuleSearchResult[]](topic13227.md) Uses {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SearchFinishedEventArgs Class](topic10317.md)   
[SearchFinishedEventArgs Members](topic10318.md)


