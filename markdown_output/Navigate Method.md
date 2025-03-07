Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Navigate Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : Navigate Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_navigateTo_
    An option specifying to where to navigate.

Glossary Item Box

Navigates the forms in a running specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Navigate( _
       ByVal _navigateTo_ As [NavigationOptions](topic10770.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim navigateTo As [NavigationOptions](topic10770.md)
    Dim value As Boolean
     
    value = instance.Navigate(navigateTo)  
  
C#|   
---|---  
      
    
    public bool Navigate( 
       [NavigationOptions](topic10770.md) _navigateTo_
    )  
  
#### Parameters

 _navigateTo_
    An option specifying to where to navigate.

#### Return Value

True if the navigation operation succeeds, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


