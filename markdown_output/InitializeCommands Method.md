![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
InitializeCommands Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic287.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IHasCommands Interface](topic282.md) : InitializeCommands Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_commandManager_
    The current command manager that can be used to control what commands are available while this object is visible.

Glossary Item Box

Called during initialization, to provide the object with the current command manager. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub InitializeCommands( _
       ByVal _commandManager_ As [ICommandButtonManager](topic124.md) _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IHasCommands](topic282.md)
    Dim commandManager As [ICommandButtonManager](topic124.md)
     
    instance.InitializeCommands(commandManager)  
  
C#|   
---|---  
      
    
    void InitializeCommands( 
       [ICommandButtonManager](topic124.md) _commandManager_
    )  
  
#### Parameters

 _commandManager_
    The current command manager that can be used to control what commands are available while this object is visible.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IHasCommands Interface](topic282.md)   
[IHasCommands Members](topic283.md)

©2024 DriveWorks Ltd. All Rights Reserved.
