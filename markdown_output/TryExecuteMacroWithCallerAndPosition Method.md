TryExecuteMacroWithCallerAndPosition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : TryExecuteMacroWithCallerAndPosition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_caller_
    The caller of the macro.

_macroName_
    The name of the macro to execute.

_clickPosition_
    The position that the macro button was clicked at.

_arguments_
    The arguments to the macro to execute.

Glossary Item Box

Executes the named macro and updates any dependencies. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryExecuteMacroWithCallerAndPosition( _
       ByVal _caller_ As String, _
       ByVal _macroName_ As String, _
       ByVal _clickPosition_ As Point, _
       ByVal ParamArray _arguments_() As Object _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim caller As String
    Dim macroName As String
    Dim clickPosition As Point
    Dim arguments() As Object
    Dim value As Boolean
     
    value = instance.TryExecuteMacroWithCallerAndPosition(caller, macroName, clickPosition, arguments)  
  
C#|   
---|---  
      
    
    public bool TryExecuteMacroWithCallerAndPosition( 
       string _caller_ ,
       string _macroName_ ,
       Point _clickPosition_ ,
       params object[] _arguments_
    )  
  
#### Parameters

 _caller_
    The caller of the macro.
_macroName_
    The name of the macro to execute.
_clickPosition_
    The position that the macro button was clicked at.
_arguments_
    The arguments to the macro to execute.

#### Return Value

True if the macro is found and executed, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)


