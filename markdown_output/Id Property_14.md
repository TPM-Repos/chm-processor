Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Id Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [DriveAppDetails Class](topic2750.md) : Id Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the unique identifier of the DriveApp. 

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
      
    
    Dim instance As [DriveAppDetails](topic2750.md)
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

[DriveAppDetails Class](topic2750.md)   
[DriveAppDetails Members](topic2751.md)


