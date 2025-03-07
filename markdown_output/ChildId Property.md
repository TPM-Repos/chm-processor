Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ChildId Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md) : ChildId Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique id of the child driven component to which the reference applies, if appropriate. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {DebugGetChildIdAsString()", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public ReadOnly Property ChildId As Nullable(Of Guid)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReadOnlyReleasedComponentReferenceDetails](topic6239.md)
    Dim value As Nullable(Of Guid)
     
    value = instance.ChildId  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {DebugGetChildIdAsString()", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Nullable<Guid> ChildId {get;}  
  
# Remarks

This value is only specified if the reference is to a driven component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md)   
[ReadOnlyReleasedComponentReferenceDetails Members](topic6240.md)


