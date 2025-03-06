TryGetTouchPointMacroAndArgument Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IPreviewDocument Interface](topic2263.md) : TryGetTouchPointMacroAndArgument Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_preview_
    The preview object to check. This can be null.

_address_
    Address of the instance you want to find the macro name and argument for.

_macroName_
    Name of the touchpoint macro if found.

_macroArgument_
    Touchpoint macro argument if found

Glossary Item Box

Takes an instance address and returns the result of its click macro and argument rules. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryGetTouchPointMacroAndArgument( _
       ByVal _preview_ As Object, _
       ByVal _address_ As String, _
       ByRef _macroName_ As String, _
       ByRef _macroArgument_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IPreviewDocument](topic2263.md)
    Dim preview As Object
    Dim address As String
    Dim macroName As String
    Dim macroArgument As String
    Dim value As Boolean
     
    value = instance.TryGetTouchPointMacroAndArgument(preview, address, macroName, macroArgument)  
  
C#|   
---|---  
      
    
    bool TryGetTouchPointMacroAndArgument( 
       object _preview_ ,
       string _address_ ,
       ref string _macroName_ ,
       ref string _macroArgument_
    )  
  
#### Parameters

 _preview_
    The preview object to check. This can be null.
_address_
    Address of the instance you want to find the macro name and argument for.
_macroName_
    Name of the touchpoint macro if found.
_macroArgument_
    Touchpoint macro argument if found

#### Return Value

True if a macro name was found. Note that macroArgument might be set despite this though.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IPreviewDocument Interface](topic2263.md)   
[IPreviewDocument Members](topic2264.md)


