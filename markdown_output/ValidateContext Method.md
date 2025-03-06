![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ValidateContext Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic142.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandContextHelper Interface](topic135.md) : ValidateContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The context to validate.

Glossary Item Box

Validates the specified context is suitable for the command. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ValidateContext( _
       ByVal _context_ As Object _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ICommandContextHelper](topic135.md)
    Dim context As Object
     
    instance.ValidateContext(context)  
  
C#|   
---|---  
      
    
    void ValidateContext( 
       object _context_
    )  
  
#### Parameters

 _context_
    The context to validate.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[CommandContextInvalidException](topic671.md)| The supplied context is invalid.  
  
# ![](dotnetimages/collapse.gif)Remarks

If the command does not expect context, and context is not a null reference (Nothing in Visual Basic), the implementation is expected to throw the [CommandContextInvalidException](topic671.md) exception.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ICommandContextHelper Interface](topic135.md)   
[ICommandContextHelper Members](topic136.md)

©2024 DriveWorks Ltd. All Rights Reserved.
