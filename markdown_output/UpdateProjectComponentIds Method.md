UpdateProjectComponentIds Method   
  
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


