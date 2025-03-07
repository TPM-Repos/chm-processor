Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Create Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectSpecificationProperties Class](topic4833.md) : Create Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_propertyName_
    The name of the specification property.

Glossary Item Box

Creates a new specification property with the given name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Create( _
       ByVal _propertyName_ As String _
    ) As [ProjectSpecificationProperty](topic4853.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectSpecificationProperties](topic4833.md)
    Dim propertyName As String
    Dim value As [ProjectSpecificationProperty](topic4853.md)
     
    value = instance.Create(propertyName)  
  
C#|   
---|---  
      
    
    public [ProjectSpecificationProperty](topic4853.md) Create( 
       string _propertyName_
    )  
  
#### Parameters

 _propertyName_
    The name of the specification property.

#### Return Value

The newly created specification property.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectSpecificationProperties Class](topic4833.md)   
[ProjectSpecificationProperties Members](topic4834.md)


