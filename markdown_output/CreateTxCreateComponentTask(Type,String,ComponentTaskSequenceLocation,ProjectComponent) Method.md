![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateComponentTask(Type,String,ComponentTaskSequenceLocation,ProjectComponent) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13030.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxCreateComponentTask Method](topic13029.md) : CreateTxCreateComponentTask(Type,String,ComponentTaskSequenceLocation,ProjectComponent) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the task to create.

_name_
    The name to give the newly created task.

_location_
    

_component_
    The component to associate the task with.

Glossary Item Box

Creates a new transaction that when executed will create a [DriveWorks.Components.Tasks.ComponentTask](topic6407.md) that is specific to the given [DriveWorks.Components.ProjectComponent](topic6183.md). 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxCreateComponentTask( _
       ByVal _type_ As Type, _
       ByVal _name_ As String, _
       ByVal _location_ As [ComponentTaskSequenceLocation](topic6406.md), _
       ByVal _component_ As [ProjectComponent](topic6183.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim type As Type
    Dim name As String
    Dim location As [ComponentTaskSequenceLocation](topic6406.md)
    Dim component As [ProjectComponent](topic6183.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateComponentTask(type, name, location, component)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateComponentTask( 
       Type _type_ ,
       string _name_ ,
       [ComponentTaskSequenceLocation](topic6406.md) _location_ ,
       [ProjectComponent](topic6183.md) _component_
    )  
  
#### Parameters

 _type_
    The type of the task to create.
_name_
    The name to give the newly created task.
_location_
    
_component_
    The component to associate the task with.

#### Return Value

A transaction that when executed will create the task using the given parameters.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13029.md)

©2024 DriveWorks Ltd. All Rights Reserved.
