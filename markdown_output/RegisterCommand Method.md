Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterCommand Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandButtonManager Interface](topic124.md) : RegisterCommand Method  
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

Registers the given command with the command manager. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function RegisterCommand( _
       ByVal _commandName_ As String, _
       ByVal _title_ As String, _
       ByVal _image_ As Image, _
       ByVal _displayHint_ As [CommandBarDisplayHint](topic657.md) _
    ) As [ICommandButton](topic115.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandButtonManager](topic124.md)
    Dim commandName As String
    Dim title As String
    Dim image As Image
    Dim displayHint As [CommandBarDisplayHint](topic657.md)
    Dim value As [ICommandButton](topic115.md)
     
    value = instance.RegisterCommand(commandName, title, image, displayHint)  
  
C#|   
---|---  
      
    
    [ICommandButton](topic115.md) RegisterCommand( 
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

The registered command.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandButtonManager Interface](topic124.md)   
[ICommandButtonManager Members](topic125.md)


