![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterSpecificationTask(Int32,String,Byte[]) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3394.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSpecifications Class](topic3355.md) > [RegisterSpecificationTask Method](topic3393.md) : RegisterSpecificationTask(Int32,String,Byte[]) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationId_
    The unique identifier of the specification for which to register the task.

_type_
    The name of the provider which understands the task.

_data_
    The task's serialized data.

Glossary Item Box

Registers a deferred specification task of the specified type. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub RegisterSpecificationTask( _
       ByVal _specificationId_ As Integer, _
       ByVal _type_ As String, _
       ByVal _data_() As Byte _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupSpecifications](topic3355.md)
    Dim specificationId As Integer
    Dim type As String
    Dim data() As Byte
     
    instance.RegisterSpecificationTask(specificationId, type, data)  
  
C#|   
---|---  
      
    
    public void RegisterSpecificationTask( 
       int _specificationId_ ,
       string _type_ ,
       byte[] _data_
    )  
  
#### Parameters

 _specificationId_
    The unique identifier of the specification for which to register the task.
_type_
    The name of the provider which understands the task.
_data_
    The task's serialized data.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupSpecifications Class](topic3355.md)   
[GroupSpecifications Members](topic3356.md)   
[Overload List](topic3393.md)

©2024 DriveWorks Ltd. All Rights Reserved.
