Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CategoryDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariableCategories Class](topic4966.md) : CategoryDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a category is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CategoryDeleted As [VariableCategoryChangedEventHandler](topic5937.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariableCategories](topic4966.md)
    Dim handler As [VariableCategoryChangedEventHandler](topic5937.md)
     
    AddHandler instance.CategoryDeleted, handler  
  
C#|   
---|---  
      
    
    public event [VariableCategoryChangedEventHandler](topic5937.md) CategoryDeleted  
  
# Event Data

The event handler receives an argument of type [VariableCategoryEventArgs](topic5851.md) containing data related to this event. The following **VariableCategoryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Category](topic5861.md)| Gets the variable category that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariableCategories Class](topic4966.md)   
[ProjectVariableCategories Members](topic4967.md)


