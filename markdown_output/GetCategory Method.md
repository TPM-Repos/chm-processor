Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCategory Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategories Class](topic4202.md) : GetCategory Method  
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
    ) As [ProjectConstantCategory](topic4219.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategories](topic4202.md)
    Dim name As String
    Dim value As [ProjectConstantCategory](topic4219.md)
     
    value = instance.GetCategory(name)  
  
C#|   
---|---  
      
    
    public [ProjectConstantCategory](topic4219.md) GetCategory( 
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

[ProjectConstantCategories Class](topic4202.md)   
[ProjectConstantCategories Members](topic4203.md)


