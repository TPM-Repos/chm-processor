![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RequiredServiceException Constructor(String)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic922.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [RequiredServiceException Class](topic915.md) > [RequiredServiceException Constructor](topic921.md) : RequiredServiceException Constructor(String)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serviceName_
    The name of the missing service.

Glossary Item Box

Initializes a new instance of the [RequiredServiceException](topic915.md) exception class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _serviceName_ As String _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim serviceName As String
     
    Dim instance As New [RequiredServiceException](topic915.md)(serviceName)  
  
C#|   
---|---  
      
    
    public RequiredServiceException( 
       string _serviceName_
    )  
  
#### Parameters

 _serviceName_
    The name of the missing service.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[RequiredServiceException Class](topic915.md)   
[RequiredServiceException Members](topic916.md)   
[Overload List](topic921.md)

©2024 DriveWorks Ltd. All Rights Reserved.
