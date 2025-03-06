![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterCommandOverride(String,CommandBarDisplayHint) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButtonManager Interface](topic124.md) > [RegisterCommandOverride Method](topic131.md) : RegisterCommandOverride(String,CommandBarDisplayHint) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The name of the command for which to get a command override.

_displayHint_
    How the button should be displayed on the command bar.

Glossary Item Box

Creates a command override object for the specified command and places it in the command bar. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Overloads Function RegisterCommandOverride( _
       ByVal _commandName_ As String, _
       ByVal _displayHint_ As [CommandBarDisplayHint](topic657.md) _
    ) As [ICommandOverride](topic180.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandButtonManager](topic124.md)
    Dim commandName As String
    Dim displayHint As [CommandBarDisplayHint](topic657.md)
    Dim value As [ICommandOverride](topic180.md)
     
    value = instance.RegisterCommandOverride(commandName, displayHint)  
  
C#|   
---|---  
      
    
    [ICommandOverride](topic180.md) RegisterCommandOverride( 
       string _commandName_ ,
       [CommandBarDisplayHint](topic657.md) _displayHint_
    )  
  
#### Parameters

 _commandName_
    The name of the command for which to get a command override.
_displayHint_
    How the button should be displayed on the command bar.

#### Return Value

The command button for the command override.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandButtonManager Interface](topic124.md)   
[ICommandButtonManager Members](topic125.md)   
[Overload List](topic131.md)


