![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AdditionalFormatGenerationFailedException Constructor(String,Exception)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic15178.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Generation Namespace](topic15094.md) > [AdditionalFormatGenerationFailedException Class](topic15170.md) > [AdditionalFormatGenerationFailedException Constructor](topic15176.md) : AdditionalFormatGenerationFailedException Constructor(String,Exception)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_message_
    A description of the exception.

_inner_
    The inner exception.

Glossary Item Box

Initializes an instance of the [AdditionalFormatGenerationFailedException](topic15170.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _message_ As String, _
       ByVal _inner_ As Exception _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim message As String
    Dim inner As Exception
     
    Dim instance As New [AdditionalFormatGenerationFailedException](topic15170.md)(message, inner)  
  
C#|   
---|---  
      
    
    public AdditionalFormatGenerationFailedException( 
       string _message_ ,
       Exception _inner_
    )  
  
#### Parameters

 _message_
    A description of the exception.
_inner_
    The inner exception.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[AdditionalFormatGenerationFailedException Class](topic15170.md)   
[AdditionalFormatGenerationFailedException Members](topic15171.md)   
[Overload List](topic15176.md)

©2024 DriveWorks Ltd. All Rights Reserved.
