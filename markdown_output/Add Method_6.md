Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedDimensionCollection Class](topic14162.md) : Add Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The DriveWorks name of the dimension.

_address_
    The SolidWorks address of the dimension.

Glossary Item Box

Adds a new dimension to the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _name_ As String, _
       ByVal _address_ As String _
    ) As [CapturedDimension](topic14154.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedDimensionCollection](topic14162.md)
    Dim name As String
    Dim address As String
    Dim value As [CapturedDimension](topic14154.md)
     
    value = instance.Add(name, address)  
  
C#|   
---|---  
      
    
    public [CapturedDimension](topic14154.md) Add( 
       string _name_ ,
       string _address_
    )  
  
#### Parameters

 _name_
    The DriveWorks name of the dimension.
_address_
    The SolidWorks address of the dimension.

#### Return Value

The newly created dimension.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedDimensionCollection Class](topic14162.md)   
[CapturedDimensionCollection Members](topic14163.md)


