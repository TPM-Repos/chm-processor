![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetTouchPointMacroAndArgument Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic2272.md)  
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

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function TryGetTouchPointMacroAndArgument( _
       ByVal _preview_ As Object, _
       ByVal _address_ As String, _
       ByRef _macroName_ As String, _
       ByRef _macroArgument_ As String _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
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

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IPreviewDocument Interface](topic2263.md)   
[IPreviewDocument Members](topic2264.md)

©2024 DriveWorks Ltd. All Rights Reserved.
