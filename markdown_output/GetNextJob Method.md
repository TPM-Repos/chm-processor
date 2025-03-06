![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetNextJob Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3601.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [JobQueue Class](topic3594.md) : GetNextJob Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tagInformation_
    The tag information for this job request.

Glossary Item Box

Gets the next job in the queue. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetNextJob( _
       ByVal _tagInformation_ As [JobRequestTagInformation](topic3604.md) _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [JobQueue](topic3594.md)
    Dim tagInformation As [JobRequestTagInformation](topic3604.md)
    Dim value As Object
     
    value = instance.GetNextJob(tagInformation)  
  
C#|   
---|---  
      
    
    public object GetNextJob( 
       [JobRequestTagInformation](topic3604.md) _tagInformation_
    )  
  
#### Parameters

 _tagInformation_
    The tag information for this job request.

#### Return Value

The next job to process.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[JobQueue Class](topic3594.md)   
[JobQueue Members](topic3595.md)

©2024 DriveWorks Ltd. All Rights Reserved.
