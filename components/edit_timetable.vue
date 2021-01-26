<template>
<table style="width: 500px">
    <tr>
        <td class="header">
            <span>Edit timetable</span>
        </td>
    </tr>
    <tr>
        <td class="panel">
            <router-link :to="{name: 'subject', params: {timetable: $route.params.timetable}}">+ Add subjects:</router-link><br />
            <br />
            <router-link :to="{name: 'room', params: {timetable: $route.params.timetable}}">+ Add rooms:</router-link><br />
            <br />
            <router-link :to="{name: 'teacher', params: {timetable: $route.params.timetable}}">+ Add teachers:</router-link><br />
			<br />
            <router-link :to="{name: 'group', params: {timetable: $route.params.timetable}}">+ Add groups:</router-link><br />
			<br />
			<br />
			<br />
			<button v-on:click="" class="ok">Get it!</button>	
        </td>
    </tr>
</table>
</template>