![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTitle Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic141.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandContextHelper Interface](topic135.md) : GetTitle Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The context which would be passed to the command's invoke method.

Glossary Item Box

Gets the context-specific title of the command. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetTitle( _
       ByVal _context_ As Object _
    ) As String  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandContextHelper](topic135.md)
    Dim context As Object
    Dim value As String
     
    value = instance.GetTitle(context)  
  
C#|   
---|---  
      
    
    string GetTitle( 
       object _context_
    )  
  
#### Parameters

 _context_
    The context which would be passed to the command's invoke method.

#### Return Value

A string containing the localized title of the command.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandContextHelper Interface](topic135.md)   
[ICommandContextHelper Members](topic136.md)

©2024 DriveWorks Ltd. All Rights Reserved.
