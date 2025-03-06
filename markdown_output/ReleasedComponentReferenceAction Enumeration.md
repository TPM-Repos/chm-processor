ReleasedComponentReferenceAction Enumeration   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) : ReleasedComponentReferenceAction Enumeration  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Specifies the action to take for a released component reference. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Enum ReleasedComponentReferenceAction 
       Inherits System.Enum  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedComponentReferenceAction](topic6146.md)  
  
C#|   
---|---  
      
    
    public enum ReleasedComponentReferenceAction : System.Enum   
  
# Members

Member| Description  
---|---  
**Delete**|  Delete the reference to the child in the parent.  
**Derive**|  Derive, the child component is derived from the parent component, e.g. additional file formats.  
**DerivedDeferred**|  Derive, the child component is derived from the parent component, e.g. additional file formats, but is to be generated separately from the parent.  
**Hide**|  Leave the reference as it is, and hide the child component.  
**None**|  Take no action, the reference entry exists only to ensure correct model generation ordering.  
**Replace**|  Replace the reference to the child in the parent and unsuppress the child component.  
**Show**|  Leave the reference as it is, and show the child component.  
**Suppress**|  Leave the reference as it is, and suppress the child component.  
**Unsuppress**|  Leave the reference as it is, and unsuppress the child component.  
  
# Inheritance Hierarchy

System.Object  
System.ValueType  
System.Enum  
**DriveWorks.Components.ReleasedComponentReferenceAction**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DriveWorks.Components Namespace](topic6089.md)


