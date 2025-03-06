       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Remove Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4154.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : Remove Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSet_
    The component set to remove.

Glossary Item Box

Removes the given component set. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Remove( _
       ByVal _componentSet_ As [ProjectComponentSet](topic4106.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
    Dim componentSet As [ProjectComponentSet](topic4106.md)
    Dim value As Boolean
     
    value = instance.Remove(componentSet)  
  
C#|   
---|---  
      
    
    public bool Remove( 
       [ProjectComponentSet](topic4106.md) _componentSet_
    )  
  
#### Parameters

 _componentSet_
    The component set to remove.

#### Return Value

True if the component set was found and removed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)

©2024 DriveWorks Ltd. All Rights Reserved.
