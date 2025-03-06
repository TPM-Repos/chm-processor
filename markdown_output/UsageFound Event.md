       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UsageFound Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Refactoring Namespace](topic10266.md) > [RenameProcess Class](topic10287.md) : UsageFound Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a usage of a name we are searching for is found. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event UsageFound As EventHandler(Of RuleSearchResultEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RenameProcess](topic10287.md)
    Dim handler As EventHandler(Of RuleSearchResultEventArgs)
     
    AddHandler instance.UsageFound, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<RuleSearchResultEventArgs> UsageFound  
  
# Event Data

The event handler receives an argument of type [RuleSearchResultEventArgs](topic13242.md) containing data related to this event. The following **RuleSearchResultEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Item](topic13248.md)| The found item from the search.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RenameProcess Class](topic10287.md)   
[RenameProcess Members](topic10288.md)


