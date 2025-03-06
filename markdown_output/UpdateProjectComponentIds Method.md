       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
UpdateProjectComponentIds Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4104.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentManager Class](topic4094.md) : UpdateProjectComponentIds Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_remappedComponentIds_
    Collection of original component identifiers to new identifiers.

Glossary Item Box

Will update the project file with the given component identifiers. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub UpdateProjectComponentIds( _
       ByVal _remappedComponentIds_ As IDictionary(Of Guid,Guid) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentManager](topic4094.md)
    Dim remappedComponentIds As IDictionary(Of Guid,Guid)
     
    instance.UpdateProjectComponentIds(remappedComponentIds)  
  
C#|   
---|---  
      
    
    public void UpdateProjectComponentIds( 
       IDictionary<Guid,Guid> _remappedComponentIds_
    )  
  
#### Parameters

 _remappedComponentIds_
    Collection of original component identifiers to new identifiers.

# Remarks

Typically used after importing a project to a new group and some component identifiers have changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentManager Class](topic4094.md)   
[ProjectComponentManager Members](topic4095.md)

©2024 DriveWorks Ltd. All Rights Reserved.
