Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CategoryParentChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategories Class](topic4202.md) : CategoryParentChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a category's parent changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event CategoryParentChanged As EventHandler(Of ConstantCategoryEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategories](topic4202.md)
    Dim handler As EventHandler(Of ConstantCategoryEventArgs)
     
    AddHandler instance.CategoryParentChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ConstantCategoryEventArgs> CategoryParentChanged  
  
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


