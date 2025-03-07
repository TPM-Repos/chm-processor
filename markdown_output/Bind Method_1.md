Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Bind Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedFormatCollection Class](topic14249.md) : Bind Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_format_
    The format to create rules for.

_parameters_
    The parameters to create rules for.

Glossary Item Box

Allows the specified format to have rules driven based on the provided parameter names. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Bind( _
       ByVal _format_ As [CapturedFormat](topic14240.md), _
       ByVal ParamArray _parameters_() As [FileFormatParameterInfo](topic13615.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedFormatCollection](topic14249.md)
    Dim format As [CapturedFormat](topic14240.md)
    Dim parameters() As [FileFormatParameterInfo](topic13615.md)
     
    instance.Bind(format, parameters)  
  
C#|   
---|---  
      
    
    public void Bind( 
       [CapturedFormat](topic14240.md) _format_ ,
       params [FileFormatParameterInfo](topic13615.md)[] _parameters_
    )  
  
#### Parameters

 _format_
    The format to create rules for.
_parameters_
    The parameters to create rules for.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedFormatCollection Class](topic14249.md)   
[CapturedFormatCollection Members](topic14250.md)


