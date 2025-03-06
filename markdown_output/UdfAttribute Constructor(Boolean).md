![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UdfAttribute Constructor(Boolean)   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7264.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Extensibility Namespace](topic7150.md) > [UdfAttribute Class](topic7256.md) > [UdfAttribute Constructor](topic7262.md) : UdfAttribute Constructor(Boolean)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_allowRunDuringLoad_
    Whether the UDF should be ran before we've started initializing the design master, which will load project elements such as form controls, variables, etc (see Remarks).

Glossary Item Box

Creates a new instance of the [UdfAttribute](topic7256.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _allowRunDuringLoad_ As Boolean _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim allowRunDuringLoad As Boolean
     
    Dim instance As New [UdfAttribute](topic7256.md)(allowRunDuringLoad)  
  
C#|   
---|---  
      
    
    public UdfAttribute( 
       bool _allowRunDuringLoad_
    )  
  
#### Parameters

 _allowRunDuringLoad_
    Whether the UDF should be ran before we've started initializing the design master, which will load project elements such as form controls, variables, etc (see Remarks).

# ![](dotnetimages/collapse.gif)Remarks

Specifying `True` for the allowRunDuringLoad parameter will cause DriveWorks to initialize the function and make it available to rules before the project opens. Because the function is initialized before the project has been fully loaded the function might not have access to any objects related to the project such as form controls, variables, etc when it is executed. This option is only recommended for functions that rely solely on the parameters passed to the function.

If allowRunDuringLoad is set to `False` (this is the default), the function will be initialized after the project has been loaded and the function will have access to the entire DriveWorks API.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[UdfAttribute Class](topic7256.md)   
[UdfAttribute Members](topic7257.md)   
[Overload List](topic7262.md)

©2024 DriveWorks Ltd. All Rights Reserved.
