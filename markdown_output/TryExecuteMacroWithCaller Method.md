![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryExecuteMacroWithCaller Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3887.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [Project Class](topic3859.md) : TryExecuteMacroWithCaller Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_caller_
    The caller of the macro.

_macroName_
    The name of the macro to execute.

_arguments_
    The arguments to the macro to execute.

Glossary Item Box

Executes the named macro and updates any dependencies. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryExecuteMacroWithCaller( _
       ByVal _caller_ As String, _
       ByVal _macroName_ As String, _
       ByVal ParamArray _arguments_() As Object _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Project](topic3859.md)
    Dim caller As String
    Dim macroName As String
    Dim arguments() As Object
    Dim value As Boolean
     
    value = instance.TryExecuteMacroWithCaller(caller, macroName, arguments)  
  
C#|   
---|---  
      
    
    public bool TryExecuteMacroWithCaller( 
       string _caller_ ,
       string _macroName_ ,
       params object[] _arguments_
    )  
  
#### Parameters

 _caller_
    The caller of the macro.
_macroName_
    The name of the macro to execute.
_arguments_
    The arguments to the macro to execute.

#### Return Value

True if the macro is found and executed, otherwise false.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Project Class](topic3859.md)   
[Project Members](topic3860.md)

©2024 DriveWorks Ltd. All Rights Reserved.
