![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CommandInvokeEventArgs Constructor   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [CommandInvokeEventArgs Class](topic691.md) : CommandInvokeEventArgs Constructor  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandContext_
    The context passed to the command's [ICommand.Invoke](topic84.md) method.

Glossary Item Box

Initializes a new instance of the [CommandInvokeEventArgs](topic691.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _commandContext_ As Object _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim commandContext As Object
     
    Dim instance As New [CommandInvokeEventArgs](topic691.md)(commandContext)  
  
C#|   
---|---  
      
    
    public CommandInvokeEventArgs( 
       object _commandContext_
    )  
  
#### Parameters

 _commandContext_
    The context passed to the command's [ICommand.Invoke](topic84.md) method.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CommandInvokeEventArgs Class](topic691.md)   
[CommandInvokeEventArgs Members](topic692.md)


