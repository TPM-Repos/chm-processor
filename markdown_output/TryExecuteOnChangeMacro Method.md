TryExecuteOnChangeMacro Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : TryExecuteOnChangeMacro Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    

_controlName_
    

_macroName_
    

_macroArgument_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub TryExecuteOnChangeMacro( _
       ByVal _e_ As [ValueChangedEventArgs](topic9575.md), _
       ByVal _controlName_ As String, _
       ByVal _macroName_ As String, _
       ByVal _macroArgument_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim e As [ValueChangedEventArgs](topic9575.md)
    Dim controlName As String
    Dim macroName As String
    Dim macroArgument As Object
     
    instance.TryExecuteOnChangeMacro(e, controlName, macroName, macroArgument)  
  
C#|   
---|---  
      
    
    protected void TryExecuteOnChangeMacro( 
       [ValueChangedEventArgs](topic9575.md) _e_ ,
       string _controlName_ ,
       string _macroName_ ,
       object _macroArgument_
    )  
  
#### Parameters

 _e_
    
_controlName_
    
_macroName_
    
_macroArgument_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


