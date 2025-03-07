Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Id Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md) : Id Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique id of the reference. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    Public ReadOnly Property Id As Guid  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReadOnlyReleasedComponentReferenceDetails](topic6239.md)
    Dim value As Guid
     
    value = instance.Id  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="Guid = {Id.ToString("B")}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    public Guid Id {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReadOnlyReleasedComponentReferenceDetails Class](topic6239.md)   
[ReadOnlyReleasedComponentReferenceDetails Members](topic6240.md)


