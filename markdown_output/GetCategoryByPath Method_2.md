Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCategoryByPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationMacroCategories Class](topic5342.md) : GetCategoryByPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_path_
    The full path to the category, delimited with the backslash character.

Glossary Item Box

Gets the category with the specified path. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCategoryByPath( _
       ByVal _path_ As String _
    ) As [SpecificationMacroCategory](topic5359.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacroCategories](topic5342.md)
    Dim path As String
    Dim value As [SpecificationMacroCategory](topic5359.md)
     
    value = instance.GetCategoryByPath(path)  
  
C#|   
---|---  
      
    
    public [SpecificationMacroCategory](topic5359.md) GetCategoryByPath( 
       string _path_
    )  
  
#### Parameters

 _path_
    The full path to the category, delimited with the backslash character.

#### Return Value

The found category or nothing if it could not be found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacroCategories Class](topic5342.md)   
[SpecificationMacroCategories Members](topic5343.md)


