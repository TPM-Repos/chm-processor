Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CategoryDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationMacroCategories Class](topic5342.md) : CategoryDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a category is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CategoryDeleted As EventHandler(Of SpecificationMacroCategoryEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacroCategories](topic5342.md)
    Dim handler As EventHandler(Of SpecificationMacroCategoryEventArgs)
     
    AddHandler instance.CategoryDeleted, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SpecificationMacroCategoryEventArgs> CategoryDeleted  
  
# Event Data

The event handler receives an argument of type [SpecificationMacroCategoryEventArgs](topic5385.md) containing data related to this event. The following **SpecificationMacroCategoryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Category](topic5395.md)| Gets the category that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacroCategories Class](topic5342.md)   
[SpecificationMacroCategories Members](topic5343.md)


