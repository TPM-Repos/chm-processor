       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove(CapturedInstance) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic14284.md)  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [CapturedInstanceCollection Class](topic14274.md) > [Remove Method](topic14282.md) : Remove(CapturedInstance) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_instance_
    The instance to remove from the collection.

Glossary Item Box

Removes the given instance from the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Remove( _
       ByVal _instance_ As [CapturedInstance](topic14267.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CapturedInstanceCollection](topic14274.md)
    Dim instance As [CapturedInstance](topic14267.md)
    Dim value As Boolean
     
    value = instance.Remove(instance)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [CapturedInstance](topic14267.md) _instance_
    )  
  
#### Parameters

 _instance_
    The instance to remove from the collection.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CapturedInstanceCollection Class](topic14274.md)   
[CapturedInstanceCollection Members](topic14275.md)   
[Overload List](topic14282.md)

©2024 DriveWorks Ltd. All Rights Reserved.
