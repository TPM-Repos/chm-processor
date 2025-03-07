Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CategoryNameChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategories Class](topic4202.md) : CategoryNameChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a category's name changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CategoryNameChanged As EventHandler(Of ConstantCategoryEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategories](topic4202.md)
    Dim handler As EventHandler(Of ConstantCategoryEventArgs)
     
    AddHandler instance.CategoryNameChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ConstantCategoryEventArgs> CategoryNameChanged  
  
# Event Data

The event handler receives an argument of type [ConstantCategoryEventArgs](topic2572.md) containing data related to this event. The following **ConstantCategoryEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Category](topic2582.md)| Gets the constant category that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstantCategories Class](topic4202.md)   
[ProjectConstantCategories Members](topic4203.md)


