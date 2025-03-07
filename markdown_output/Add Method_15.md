Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedAnnotationCollection Class](topic14756.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    

_address_
    

_type_
    

_value_
    

Glossary Item Box

Adds a new annotation. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _address_ As String, _
       ByVal _type_ As SolidWorks.Interop.swconst.swAnnotationType_e, _
       ByVal _value_ As String _
    ) As [ReleasedAnnotation](topic14746.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedAnnotationCollection](topic14756.md)
    Dim name As String
    Dim address As String
    Dim type As SolidWorks.Interop.swconst.swAnnotationType_e
    Dim value As String
    Dim value As [ReleasedAnnotation](topic14746.md)
     
    value = instance.Add(name, address, type, value)  
  
C#|   
---|---  
      
    
    public [ReleasedAnnotation](topic14746.md) Add( 
       string _name_ ,
       string _address_ ,
       SolidWorks.Interop.swconst.swAnnotationType_e _type_ ,
       string _value_
    )  
  
#### Parameters

 _name_
    
_address_
    
_type_
    
_value_
    

#### Return Value

The newly created annotation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedAnnotationCollection Class](topic14756.md)   
[ReleasedAnnotationCollection Members](topic14757.md)


