Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ControlTypeResolverDelegate Delegate   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel.Serialization Namespace](topic9591.md) : ControlTypeResolverDelegate Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_fullTypeName_
    The plugin-assembly qualified type name of the control.

Glossary Item Box

Represents a method which can resolve a control type based on its plugin-assembly qualified type name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Function ControlTypeResolverDelegate( _
       ByVal _fullTypeName_ As String _
    ) As Type  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [ControlTypeResolverDelegate](topic9625.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate Type ControlTypeResolverDelegate( 
       string _fullTypeName_
    )  
  
#### Parameters

 _fullTypeName_
    The plugin-assembly qualified type name of the control.

#### Return Value

The type of the control or a null reference if no control was found.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlTypeResolverDelegate Members](topic9625.md)   
[DriveWorks.Forms.DataModel.Serialization Namespace](topic9591.md)


