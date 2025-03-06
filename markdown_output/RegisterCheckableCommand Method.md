![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterCheckableCommand Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic129.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButtonManager Interface](topic124.md) : RegisterCheckableCommand Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandName_
    The culture invariant name of the command.

_title_
    The localized title of the command.

_image_
    An image handle which provides a UI representation of the command.

_displayHint_
    How the button should be displayed on the command bar.

Glossary Item Box

Registers a checkable command with the command manager. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RegisterCheckableCommand( _
       ByVal _commandName_ As String, _
       ByVal _title_ As String, _
       ByVal _image_ As Image, _
       ByVal _displayHint_ As [CommandBarDisplayHint](topic657.md) _
    ) As [ICheckableCommandButton](topic66.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandButtonManager](topic124.md)
    Dim commandName As String
    Dim title As String
    Dim image As Image
    Dim displayHint As [CommandBarDisplayHint](topic657.md)
    Dim value As [ICheckableCommandButton](topic66.md)
     
    value = instance.RegisterCheckableCommand(commandName, title, image, displayHint)  
  
C#|   
---|---  
      
    
    [ICheckableCommandButton](topic66.md) RegisterCheckableCommand( 
       string _commandName_ ,
       string _title_ ,
       Image _image_ ,
       [CommandBarDisplayHint](topic657.md) _displayHint_
    )  
  
#### Parameters

 _commandName_
    The culture invariant name of the command.
_title_
    The localized title of the command.
_image_
    An image handle which provides a UI representation of the command.
_displayHint_
    How the button should be displayed on the command bar.

#### Return Value

The registered checkable command.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandButtonManager Interface](topic124.md)   
[ICommandButtonManager Members](topic125.md)

©2024 DriveWorks Ltd. All Rights Reserved.
