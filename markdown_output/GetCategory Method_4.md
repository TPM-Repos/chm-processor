Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [SpecificationMacroCategories Class](topic5342.md) : GetCategory Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the category to retrieve.

Glossary Item Box

Gets the named category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCategory( _
       ByVal _name_ As String _
    ) As [SpecificationMacroCategory](topic5359.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacroCategories](topic5342.md)
    Dim name As String
    Dim value As [SpecificationMacroCategory](topic5359.md)
     
    value = instance.GetCategory(name)  
  
C#|   
---|---  
      
    
    public [SpecificationMacroCategory](topic5359.md) GetCategory( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the category to retrieve.

# Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if the specified category is not found.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacroCategories Class](topic5342.md)   
[SpecificationMacroCategories Members](topic5343.md)


